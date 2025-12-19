---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/merge-vhd?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Merge-VHD
---

# 合并VHD文件

## 摘要
合并虚拟硬盘。

## 语法

```
Merge-VHD [-Path] <String> [[-DestinationPath] <String>] [-Force] [-AsJob] [-Passthru]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Merge-VHD** cmdlet 用于合并差异化虚拟硬盘链中的虚拟硬盘。合并操作是从指定的源子硬盘到指定的目标子硬盘进行的。

合并操作是离线进行的；在启动合并过程时，必须确保虚拟硬盘链未被连接（即不可处于正在使用状态）。

## 示例

### 示例 1
```
PS C:\> Merge-VHD -Path c:\test\Child4.vhdx -DestinationPath c:\test\Child2.vhdx
```

这个示例将Child4中的虚拟硬盘合并到Child2中，从而形成一个虚拟硬盘链：Child4是Child3的子盘，Child3是Child2的子盘，Child2是Child1的子盘，而Child1则是Parent的子盘。所有相关的虚拟硬盘文件都位于c:\test目录下。该操作会将Child4和Child3中的所有数据合并到Child2中。虽然Child4.vhdx和Child3.vhdx文件本身不会被删除，但在操作完成后，它们将不再被视为有效的虚拟硬盘文件。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。

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
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于合并虚拟硬盘的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行识别。默认值是本地计算机。可以通过使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationPath
指定虚拟硬盘链中作为合并命令目标的分区的路径。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
直接运行该cmdlet，而不会提示用户进行确认。

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

### -Passthru
指定将某个对象传递给表示合并后的虚拟硬盘的流水线（pipeline）。

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
指定虚拟硬盘链中作为合并命令来源的子文件的路径。如果指定了文件名或相对路径，那么虚拟硬盘的路径将相对于当前工作目录进行计算。

```yaml
Type: String
Parameter Sets: (All)
Aliases: FullName

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行时会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### VHDObject

## 输出

### Microsoft.Vhd.PowerShell.VirtualHardDisk

## 备注

## 相关链接

