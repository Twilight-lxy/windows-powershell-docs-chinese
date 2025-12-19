---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: FsrmQuota.cdxml-help.xml
Module Name: FileServerResourceManager
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/fileserverresourcemanager/new-fsrmquota?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-FsrmQuota
---

# 新Fsm配额设置

## 摘要
创建一个FSRM配额。

## 语法

```
New-FsrmQuota [-Path] <String> [-Description <String>] [-Template <String>] [-Size <UInt64>] [-Disabled]
 [-SoftLimit] [-Threshold <CimInstance[]>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`New-FsrmQuota` cmdlet 用于在服务器上创建文件服务器资源管理器（FSRM）的配额。该配额适用于指定的目录及其所有子目录（递归应用）。在层次结构中位置较高的文件夹上设置的配额，会进一步限制较低层级文件夹上的配额设置。

## 示例

#### 示例 1：设置硬性配额限制
```
PS C:\> New-FsrmQuota -Path "C:\Shares" -Description "limit usage to 1 GB." -Size 1GB
```

这个命令会在 C:\Shares 目录下创建一个配额，并为该配额添加描述。该配额被设置为一个固定的大小限制（1GB），且不包含任何阈值设定。固定大小的配额会阻止用户在磁盘空间达到上限后继续保存文件；当数据量达到每个预设的阈值时，系统会生成相应的通知。

### 示例 2：根据配额模板创建配额
```
PS C:\> New-FsrmQuota -Path "C:\Shares" -Description "limit usage to 100 MB based on template." -Template "100 MB Limit"
```

此命令根据名为“100 MB Limit”的模板，在C:\Shares目录上创建一个配额。该命令为配额指定了一个与模板中描述不同的说明文本。该配额被设置为硬性限制，大小为100 MB，并且不包含任何阈值（即没有达到某个使用量时自动调整配额的限制）。

#### 示例 3：创建一个软限制配额，用于运行命令
```
The first command creates an FSRM action object and stores the results in the $Action variable. The action indicates that when an associated event occurs, the server run Cmd.exe with the specified parameters. The command specifies that server record errors codes from the executed command in the error log.
PS C:\> $Action = New-FsrmAction -Type Command -Command "c:\windows\system32\cmd.exe" -CommandParameters "echo [source file path] >> c:\log.txt" -ShouldLogError

The second command creates a threshold object and stores the results in the $Threshold variable. The command specifies the percentage of the quota limit at which to execute the action, and specifies the action stored in the $Action variable.
PS C:\> $Threshold = New-FsrmQuotaThreshold -Percentage 90 -Action $action

The third command creates a quota on C:\Shares and specifies the threshold stored in the $Threshold variable. The *SoftLimit* parameter indicates the quota reports on the disk usage with respect to the size limit and run thresholds, but does not enforce the size limit.
PS C:\> New-FsrmQuota -Path "C:\Shares" -Size 128MB -Threshold $Threshold -SoftLimit
```

这个示例在 C:\Shares 目录下创建了一个新的配额设置。该配额的软限制为 128MB，使用率达到 90% 时会触发警告（阈值），并且会执行一个自定义命令。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet将在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否要继续执行该操作。

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

### -Description
为配额指定一个描述性说明。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Disabled
表示该配额已被禁用。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Path
指定一个有效的本地文件夹路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Size
指定配额模板所强制执行的空格限制。

```yaml
Type: UInt64
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SoftLimit
这表示配额报告会显示磁盘使用情况与大小限制及运行阈值之间的关系，但并不会强制实施该大小限制。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Template
指定服务器上一个配额模板（quota template）的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Threshold
指定一个阈值对象的数组。

`threshold` 对象定义了在文件操作过程中允许使用的空间占可用空间的百分比，以及当配额达到该阈值时服务器会执行的一系列操作。要使系统在配额被超出时执行相应的操作，请将 `threshold` 设置为 100（即 100%）。您可以使用 `New-FsrmQuotaThreshold` cmdlet 来创建一个 `threshold` 对象。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的限速值。该限速值仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.UInt64

### System.Management Automation.SwitchParameter

### Microsoft.ManagementInfrastructure.CimInstance[]

## 输出

### System.Object

## 备注

## 相关链接

[Get-FsrmQuota](./Get-FsrmQuota.md)

[Remove-FsrmQuota](./Remove-FsrmQuota.md)

[Reset-FsrmQuota](./Reset-FsrmQuota.md)

[Set-FsrmQuota](./Set-FsrmQuota.md)

[更新-FsrmQuota](./Update-FsrmQuota.md)

