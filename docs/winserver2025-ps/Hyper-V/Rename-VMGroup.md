---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/rename-vmgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-VMGroup
---

# 重命名 VMGroup

## 摘要
重命名虚拟机组。

## 语法

### 名称（默认值）
```
Rename-VMGroup [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String[]> [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ID
```
Rename-VMGroup [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Rename-VMGroup [-VMGroup] <VMGroup[]> [-NewName] <String> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Rename-VMGroup` cmdlet 用于重命名虚拟机组。

## 示例

#### 示例 1：重命名一个群组
```
PS C:\> Rename-VMGroup -Name "TestGroup" -NewName "Group01"
```

这个命令将名为“TestGroup”的组重命名为“Group01”。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全限定域名来进行标识。默认值为本地计算机。可以通过使用“localhost”或点（.）来明确指出是本地计算机。

```yaml
Type: String[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

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
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定该 cmdlet 用于重命名的虚拟机组的唯一标识符。

```yaml
Type: Guid
Parameter Sets: Id
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个虚拟机组名称数组，该cmdlet将对其进行重命名。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewName
指定虚拟机组的新名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示该 cmdlet 返回的是它所重命名的 **Microsoft.HyperV.PowShell.VMGroup** 对象。

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

### -VMGroup
指定一个虚拟机组数组，该 cmdlet 将对这些虚拟机组进行重命名。要获取一个 **VMGroup** 对象，请使用 **Get-VMGroup** cmdlet。

```yaml
Type: VMGroup[]
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行该 cmdlet。

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

## 输出

### Microsoft.HyperV.PowerShell.VMGroup
如果指定了 `Passthru` 参数，此 cmdlet 会返回一个 `Microsoft.HyperV.PowerShell.VMGroup` 对象。

## 备注

## 相关链接

[Get-VMGroup](./Get-VMGroup.md)

[New-VMGroup](./New-VMGroup.md)

[Remove-VMGroup](./Remove-VMGroup.md)

