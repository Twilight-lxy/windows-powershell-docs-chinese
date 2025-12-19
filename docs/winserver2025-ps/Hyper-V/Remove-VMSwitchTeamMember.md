---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmswitchteammember?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMSwitchTeamMember
---

# 删除VMSwitch团队成员

## 摘要
将某个成员从虚拟机交换机团队中移除。

## 语法

### SwitchName_NetAdapterName（默认值）
```
Remove-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitchName] <String[]> [-NetAdapterName <String[]>]
 [-Passthru] [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### SwitchName_NetAdapterInterfaceDescription
```
Remove-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitchName] <String[]>
 [-NetAdapterInterfaceDescription <String[]>] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterInterfaceDescription
```
Remove-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitch] <VMSwitch[]>
 [-NetAdapterInterfaceDescription <String[]>] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SwitchObject_NetAdapterName
```
Remove-VMSwitchTeamMember [-ComputerName <String[]>] [-VMSwitch] <VMSwitch[]> [-NetAdapterName <String[]>]
 [-Passthru] [-CimSession <CimSession[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-VMSwitchTeamMember` cmdlet 用于从虚拟机交换机团队中移除虚拟网络适配器。

## 示例

#### 示例 1：从交换机组中删除网络适配器
```
PS C:\> $VMSwitch = Get-VMSwitch -Name "Switch03"
PS C:\> Remove-VMSwitchTeamMember -VMSwitch $VMSwitch -NetAdapterName "Adapter01","Adapter04"
```

第一个命令获取名为“Switch03”的虚拟交换机，并将该对象存储在 `$VMSwitch` 变量中。

第二个命令会将名为Adapter01和Adapter04的网络适配器从**$VMSwitch**中的交换机中移除（即不再将它们作为团队成员纳入该交换机的管理范围）。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

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
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

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
指定一个虚拟网络适配器接口描述的数组，该cmdlet会从交换机组中删除这些适配器。

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
指定一个虚拟网络适配器名称数组，该cmdlet将从交换机团队中删除这些适配器。

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
表示此cmdlet返回了它所修改的`Microsoft.HyperV.PowerShell.VMSwitch`对象。

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
指定一个虚拟交换机数组，该cmdlet将从这些虚拟交换机中移除网络适配器。要获取一个**VMSwitch**对象，请使用**Get-VMSwitch** cmdlet。

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
指定一个虚拟交换机名称数组，该cmdlet将从这些虚拟交换机中删除网络适配器。

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
展示了如果运行该cmdlet会发生什么情况。但实际上这个cmdlet并没有被执行。

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

### Microsoft.HyperV POWERShell.VMSwitch[]
如果指定了 **Passthru** 参数，此 cmdlet 会返回一个包含 **VMSwitch** 对象的数组。

## 备注

## 相关链接

[Add-VMSwitchTeamMember](./Add-VMSwitchTeamMember.md)

[Get-VMSwitch](./Get-VMSwitch.md)

