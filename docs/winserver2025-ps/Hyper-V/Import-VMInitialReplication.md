---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/import-vminitialreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Import-VMInitialReplication
---

# 导入虚拟机初始复制相关代码

## 摘要
在使用外部介质作为源时，导入Replica虚拟机的初始复制文件以完成初始复制过程。

## 语法

### VMName（默认值）
```
Import-VMInitialReplication [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-Path] <String> [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Import-VMInitialReplication [-VM] <VirtualMachine[]> [-Path] <String> [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 虚拟机复制（VMReplication）
```
Import-VMInitialReplication [-VMReplication] <VMReplication[]> [-Path] <String> [-AsJob] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Import-VMInitialReplication` cmdlet 用于在副本服务器上导入初始复制文件。当使用外部资源作为这些文件的来源时，该命令可完成虚拟机的初始复制过程。

## 示例

### 示例 1
```
PS C:\> Import-VMInitialReplication VM01 d:\VMImportLocation\VM01
```

这个示例从位置 d:\VMImportLocation\VM01 导入了名为 VM01 的虚拟机的初始复制文件。

### 示例 2
```
PS C:\> Get-VMReplication | ForEach-Object {$path = "D:\OOBLoc\" + $_.VMName + "_" + $_.VMID; if (Test-Path $path -PathType Container) {Import-VMInitialReplication $_ $path}}
```

这个示例使用位于 D:\OOBLoc\ 目录中的文件，为一组虚拟机导入初始的复制文件。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于导入初始复制文件的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值为本地计算机。可以使用 `localhost` 或句点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此cmdlet返回一个`Microsoft.HyperV.PowerShell.VirtualMachine`对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定要导入的初始复制文件的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases: IRLoc

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定用于导入初始复制文件的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要导入初始复制文件的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMReplication
指定用于导入初始复制文件的虚拟机复制对象。

```yaml
Type: VMReplication[]
Parameter Sets: VMReplication
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上该cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VirtualMachine
如果指定了 **-PassThru**。

## 备注

## 相关链接

