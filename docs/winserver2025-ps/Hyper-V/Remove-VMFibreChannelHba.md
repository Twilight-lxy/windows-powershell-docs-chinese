---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmfibrechannelhba?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMFibreChannelHba
---

# 删除 VMFibreChannelHba

## 摘要
从虚拟机中移除一个光纤通道（Fibre Channel）主机总线适配器。

## 语法

### VMFibreChannelHba（默认值）
```
Remove-VMFibreChannelHba [-VMFibreChannelHba] <VMFibreChannelHba[]> [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMName 和 WWN
```
Remove-VMFibreChannelHba [-VMName] <String> [-WorldWideNodeNameSetA] <String> [-WorldWidePortNameSetA] <String>
 [-WorldWideNodeNameSetB] <String> [-WorldWidePortNameSetB] <String> [-Passthru] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMFibreChannelHba` 这个 cmdlet 用于从虚拟机中删除一个光纤通道（Fibre Channel）主机总线适配器。

## 示例

### 示例 1
```
PS C:\> Get-VMFibreChannelHba -VMName MyVM | Remove-VMFibreChannelHba
```

从虚拟机 MyVM 中移除一个光纤通道（Fibre Channel）主机总线适配器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个要从中卸载光纤通道主机总线适配器的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机；可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定将某个对象传递给流水线处理，该对象代表被移除的光纤通道（Fibre Channel）主机总线适配器。

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

### -VMFibreChannelHba
指定一个或多个需要从虚拟机中删除的 Fibre Channel 主总线适配器。

```yaml
Type: VMFibreChannelHba[]
Parameter Sets: VMFibreChannelHba
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要从中移除光纤通道（Fibre Channel）主机总线适配器的虚拟机。

```yaml
Type: String
Parameter Sets: VMName and WWN
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被执行。

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

### -WorldWideNodeNameSetA
指定要与要移除的 Fibre Channel 主总线适配器相关联的地址集 A 的全球节点名称（即 WWN）。

```yaml
Type: String
Parameter Sets: VMName and WWN
Aliases: Wwnn1

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWideNodeNameSetB
指定要与要卸载的 Fibre Channel 主机总线适配器关联的地址集 B 的全球唯一节点名称（World Wide Node Name）。

```yaml
Type: String
Parameter Sets: VMName and WWN
Aliases: Wwnn2

Required: True
Position: 3
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortNameSetA
指定要与要卸载的 Fibre Channel 主总线适配器相关联的地址集 A 的全球通用端口名称（World Wide Port name）。

```yaml
Type: String
Parameter Sets: VMName and WWN
Aliases: Wwpn1

Required: True
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortNameSetB
指定要与要卸载的Fibre Channel主机总线适配器关联的地址集B的全球通用端口号（WWPN）。

```yaml
Type: String
Parameter Sets: VMName and WWN
Aliases: Wwpn2

Required: True
Position: 4
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMFibreChannelHba
如果指定了**-PassThru**选项……

## 备注

## 相关链接

