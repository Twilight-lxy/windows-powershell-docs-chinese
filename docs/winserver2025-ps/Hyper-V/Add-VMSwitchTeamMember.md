---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmswitchteammember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMSwitchTeamMember
---

# Add-VMSwitchTeamMember

## 摘要
向虚拟交换机组中添加成员。

## 语法

### SwitchName_NetAdapterName（默认值）
```
Add-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitchName] <String[]> [-NetAdapterName <String[]>]
 [-Passthru] [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### SwitchName_NetAdapterInterfaceDescription
```
Add-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitchName] <String[]>
 [-NetAdapterInterfaceDescription <String[]>] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterInterfaceDescription
```
Add-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitch] <VMSwitch[]>
 [-NetAdapterInterfaceDescription <String[]>] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterName
```
Add-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitch] <VMSwitch[]> [-NetAdapterName <String[]>]
 [-Passthru] [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-VMSwitchTeamMember` cmdlet 可将适配器添加为虚拟交换机团队的成员。

## 示例

### 示例 1：将网络适配器添加到交换机组中
```
PS C:\> $VMSwitch = Get-VMSwitch -Name "Switch03"
PS C:\> Add-VMSwitchTeamMember -VMSwitch $VMSwitch -NetAdapterName "Adapter01","Adapter04"
```

第一个命令获取名为“Switch03”的虚拟交换机团队，并将其存储在 `$VMSwitch` 变量中。

第二条命令将名为Adapter01和Adapter04的网络适配器添加为团队成员，加入到**$VMSwitch**中的交换机团队中。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名来进行指定。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases: PSComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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

### -NetAdapterInterfaceDescription
指定一个接口描述数组，这些描述对应于该cmdlet要添加到交换机组中的虚拟网络适配器。

```yaml
Type: String[]
Parameter Sets: SwitchName_NetAdapterInterfaceDescription, SwitchObject_NetAdapterInterfaceDescription
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NetAdapterName
指定一个虚拟网络适配器名称数组，该cmdlet会将这些适配器添加到交换机团队中。

```yaml
Type: String[]
Parameter Sets: SwitchName_NetAdapterName, SwitchObject_NetAdapterName
Aliases: InterfaceAlias

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此 cmdlet 返回它所修改的 **Microsoft.HyperV.PowerShell.VMSwitch** 对象。

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

### -VMSwitch
指定一个虚拟交换机数组，该数组将由此cmdlet进行配置。要获取一个**VMSwitch**对象，请使用**Get-VMSwitch** cmdlet。

```yaml
Type: VMSwitch[]
Parameter Sets: SwitchObject_NetAdapterInterfaceDescription, SwitchObject_NetAdapterName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSwitchName
指定一个虚拟交换机名称数组，该数组中的虚拟交换机将由此cmdlet进行配置。

```yaml
Type: String[]
Parameter Sets: SwitchName_NetAdapterName, SwitchName_NetAdapterInterfaceDescription
Aliases: SwitchName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMSwitch
如果指定了 **Passthru** 参数，此 cmdlet 会返回一个 **VMSwitch** 对象。

## 备注

## 相关链接

[Remove-VMSwitchTeamMember](./Remove-VMSwitchTeamMember.md)

[Get-VMSwitch](./Get-VMSwitch.md)

