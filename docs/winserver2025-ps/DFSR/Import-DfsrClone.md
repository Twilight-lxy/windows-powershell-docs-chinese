---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: DfsrPowerShell.dll-Help.xml
Module Name: DFSR
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dfsr/import-dfsrclone?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-DfsrClone
---

# Import-DfsrClone

## 摘要
导入已克隆的DFS复制数据库及卷配置设置。

## 语法

```
Import-DfsrClone [-Volume] <String> [-Path] <String> [-Force] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Import-DfsrClone** cmdlet 用于从另一台计算机导入分布式文件系统（DFS）复制数据库以及指定卷的配置 XML 文件设置，以便将 해당 数据库克隆到本地计算机上。每个包含已复制文件夹内容的卷上都存在 DFS 复制数据库，且所有这些数据库共同构成了一个完整的数据库系统（该数据库中包含了所有被复制文件夹的引用信息）。运行此 cmdlet 会触发 DFS 复制服务中的导入操作，并等待服务完成整个过程。您可以使用 **Get-DfsrCloneState** 命令来监控导入进度。

重要提示：在 Windows Server 2012 R2 中，DFS 复制功能不支持克隆 SYSVOL 文件系统或只读副本。导出过程会自动跳过已复制的文件夹。对于一台计算机来说，您一次只能导入或导出一个数据库。

请按照推荐和支持的步骤来执行DFS复制数据库克隆操作。有关更多信息，请访问以下Microsoft网站：[http://go.microsoft.com/fwlink/?LinkId=302005](https://go.microsoft.com/fwlink/?LinkId=302005)。  
“上游”（upstream）指的是作为复制文件数据及DFS复制数据库权威来源的服务器；而“下游”（downstream）则是指从该权威服务器复制的非权威服务器。

## 示例

### 示例 1：克隆并导入一个DFS复制数据库
```
PS C:\> Import-DfsrClone -Volume "C:" -Path C:\DfsRClone
This operation will import the database and clone DFSR. It can take a long time to complete. Use Get-DfsrCloneState or
DFSR event 2404 to determine when the import has succeeded. Volume:
c:\ Path: C:\Dfsrclone
Are you sure you want to continue to import the database clone? [Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"):Y
```

此命令将DFS复制数据库和卷配置的XML文件从C:\DfsRClone文件夹克隆到C:驱动器上。

#### 示例 2：导入一个 DFS 复制数据库并定期检查其状态
```
PS C:\> Import-DfsrClone -Volume "C:" -Path C:\DfsRClone
PS C:\> Get-DfsrCloneState
PS C:\> Get-DfsrCloneState
PS C:\> Get-DfsrCloneState
```

这个示例导入了一个 DFS 复制数据库的克隆副本，然后使用 **Get-DfsrCloneState** cmdlet 定期检查复制操作的状态，直到复制操作完成。

第一个命令使用了 **Import-DfsrClone** cmdlet 来启动导入过程。您需要打开另一个 Windows PowerShell 控制台，或者按 CTRL+C 退出 **Import-DfsrClone** cmdlet。即使该 cmdlet 停止运行，克隆操作仍会在服务器上继续进行。

第二个命令使用了 **Get-DfsrCloneState** cmdlet 来检查导入进程的状态。命令执行完成后，会显示相应的输出结果。

第三个命令使用了 **Get-DfsrCloneState** cmdlet 来检查导入进程的状态。输出结果表明导入操作已经成功完成。

#### 示例 3：导出和导入数据库
```
PS C:\> New-DfsReplicationGroup "RG05" | New-DfsReplicatedFolder -FolderName "RF05" | Add-DfsrMember -ComputerName "SRV01"
PS C:\> Set-DfsrMembership -ComputerName "SRV01" -ContentPath "C:\Rf05" -PrimaryMember $True -FolderName "RF05"
PS C:\> Update-DfsrConfigurationFromAD
PS C:\> New-Item -Path C:\DfsRClone -Type Directory
PS C:\> Export-DfsrClone -Volume "C:" -Path "C:\DfsRClone"
PS C:\> Robocopy.exe C:\Rf05 \\srv02\c$\Rf5 /E /B /COPYALL /R:6 /W:5 /MT:64 /XD DfsrPrivate /TEE /LOG+:preseed.log
PS C:\> Robocopy.exe C:\DfsRClone \\srv02\c$\DfsRClone /B
PS C:\> RD "C:\system volume information\dfsr" -Force -Recurse
PS C:\> Import-DfsrClone -Volume "C:" -Path C:\DfsRClone
PS C:\> Get-DfsrCloneState
PS C:\> Add-DfsrMember -GroupName "RG05" -ComputerName "SRV02" | Set-DfsrMembership -FolderName "RF05" -ContentPath "C:\Rf05"
PS C:\> Add-DfsrConnection -GroupName "RG05" -SourceComputerName "SRV01" -DestinationComputerName "SRV02"
PS C:\> Update-DfsrConfigurationFromAD
```

这个示例演示了从开始到结束的整个过程：将 SRV01 及其在 C:\ 盘上复制的 RF05 文件夹克隆到服务器 SRV02 上。前七个命令在上游服务器上执行，其余命令则在下游服务器上执行。

第一个命令是在上游服务器上执行的，它使用 **New-DfsReplicationGroup** cmdlet 创建一个名为 RG05 的复制组。该命令的输出结果被传递给 **New-DfsReplicatedFolder** cmdlet，用于创建一个名为 RF05 的文件夹；接着，这个输出结果又被传递给 **Add-DfsrMember** cmdlet，以便将名为 SRV01 的计算机添加为该复制组的成员。

第二个命令在上游服务器上使用 **Set-DfsrMembership** cmdlet 来修改名为 SRV01 的计算机的成员资格。

第三个命令是在上游服务器上执行的，它使用 **Update-DfsrConfigurationFromAD** cmdlet 来更新源服务器上的 DFS 复制配置。

第四条命令是在上游服务器上执行的，它使用 **New-Item** cmdlet 在路径 C:\DfsRClone 下创建一个新目录。

第五条命令是在上游服务器上执行的，它使用 **Export-DfsrClone** cmdlet 来导出一个卷（即一个数据存储单元）。

第六条命令是在上游服务器上执行的，它使用 Robocopy 将复制过来的文件夹目录结构复制到目标服务器上。

第七条命令是在上游服务器上执行的，它使用 Robocopy 工具将 C:\DfsRClone 目录复制到目标服务器上。

第八条命令是在下游服务器上执行的，它使用RD（Remote Desktop）来删除复制目录（如果该目录存在的话）。

第九条命令是在下游服务器上执行的，它使用 **Import-DfsrClone** cmdlet 将数据库和卷配置导入到目标服务器中。

第十条命令是在下游服务器上执行的，它使用 **Get-DfsrCloneState** cmdlet 来验证导入过程的完成情况。

第十一条命令是在下游服务器上执行的，它使用 **Add-DfsrMember** cmdlet 在目标服务器上创建一个新的组。该命令会将这个 cmdlet 的输出结果传递给 **Set-DfsrMembership** cmdlet，以便为该复制的文件夹组添加成员资格（即允许该文件夹组访问共享资源）。

第十二条命令是在下游服务器上执行的，它使用 **Add-DfsrConnection** cmdlet 来为目标服务器添加一个连接。

最后一个命令是在下游服务器上执行的，它使用 **Update-DfsrConfigurationFromAD** cmdlet 来更新目标服务器上的 DFS 复制配置。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您确认是否要继续操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而不需要用户确认。此参数适用于脚本化的克隆操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定用于读取导出的 DFS 复制数据库和卷配置 XML 文件的位置。在导出 DFS 复制数据库之后、但在执行导入克隆操作之前，必须将复制文件夹的内容填充到下游服务器中。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SourceFolderPath

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Volume
指定一个驱动器字母或挂载点，该位置包含已填充的DFS复制文件内容。在导入完成后，这个卷中会存储之前导出的数据库。在导出DFS复制数据库之后、但在执行导入克隆操作之前，必须将复制的文件夹内容填充到下游服务器中。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行这个 cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### 无

## 备注

## 相关链接

[Export-DfsrClone](./Export-DfsrClone.md)

