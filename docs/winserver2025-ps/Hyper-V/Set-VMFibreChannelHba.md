---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmfibrechannelhba?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMFibreChannelHba
---

# 设置 VMFibreChannelHba

## 摘要
在虚拟机上配置一个光纤通道（Fibre Channel）主机总线适配器。

## 语法

### 只使用虚拟机名称（VMName）和SAN存储（默认设置）
```
Set-VMFibreChannelHba [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-WorldWideNodeNameSetA] <String> [-WorldWidePortNameSetA] <String>
 [-WorldWideNodeNameSetB] <String> [-WorldWidePortNameSetB] <String> -SanName <String> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 输入虚拟机名称（VMName）并生成 Worldwide Name (WWN)
```
Set-VMFibreChannelHba [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-WorldWideNodeNameSetA] <String> [-WorldWidePortNameSetA] <String>
 [-WorldWideNodeNameSetB] <String> [-WorldWidePortNameSetB] <String> [-GenerateWwn] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 虚拟机名称（VMName）和手动分配的世界广域网标识符（WWN）
```
Set-VMFibreChannelHba [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-WorldWideNodeNameSetA] <String> [-WorldWidePortNameSetA] <String>
 [-WorldWideNodeNameSetB] <String> [-WorldWidePortNameSetB] <String> [-NewWorldWideNodeNameSetA <String>]
 [-NewWorldWidePortNameSetA <String>] [-NewWorldWideNodeNameSetB <String>] [-NewWorldWidePortNameSetB <String>]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 创建对象并生成WWN（World Wide Number）
```
Set-VMFibreChannelHba [-VMFibreChannelHba] <VMFibreChannelHba> [-GenerateWwn] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 对象和手动WWN（World Wide Name）
```
Set-VMFibreChannelHba [-VMFibreChannelHba] <VMFibreChannelHba> [-NewWorldWideNodeNameSetA <String>]
 [-NewWorldWidePortNameSetA <String>] [-NewWorldWideNodeNameSetB <String>] [-NewWorldWidePortNameSetB <String>]
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 仅限对象存储（Object and Only SAN）
```
Set-VMFibreChannelHba [-VMFibreChannelHba] <VMFibreChannelHba> -SanName <String> [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Set-VMFibreChannelHba` cmdlet 用于配置虚拟机上的光纤通道（Fibre Channel）主机总线适配器。

## 示例

### 示例 1
```
PS C:\> Get-VMFibreChannelHba -VMName MyVM | Set-VMFibreChannelHba -GenerateWwn
```

在名为“MyVM”的虚拟机上配置一个光纤通道（Fibre Channel）主机总线适配器，并设置其全球通用名称（World Wide Names）自动生成。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置光纤通道主机总线适配器的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值为本地计算机；可以通过使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GenerateWwn
指定集合A和集合B的全球通用名称（World Wide Names）需要自动生成。当指定了此参数时，就不能使用参数**WorldWideNodeNameSetA**、**WorldWideNodeNameSetB**、**WorldWidePortNameSetA**以及**WorldWidePortNameSetB**了。

```yaml
Type: SwitchParameter
Parameter Sets: VMName And Generate WWN, Object And Generate WWN
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewWorldWideNodeNameSetA
指定要与光纤通道主机总线适配器关联的地址集A的全球节点名称（World Wide Node Name）。

```yaml
Type: String
Parameter Sets: VMName And Manual WWN, Object And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewWorldWideNodeNameSetB
指定将与光纤通道主机总线适配器关联的地址集B的全球唯一节点名称（World Wide Node Name）。

```yaml
Type: String
Parameter Sets: VMName And Manual WWN, Object And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewWorldWidePortNameSetA
指定要与光纤通道主机总线适配器关联的地址集A的全球通用端口号（World Wide Port Name）。

```yaml
Type: String
Parameter Sets: VMName And Manual WWN, Object And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewWorldWidePortNameSetB
指定要与光纤通道主机总线适配器关联的地址集B的全球通用端口名称（World Wide Port Name）。

```yaml
Type: String
Parameter Sets: VMName And Manual WWN, Object And Manual WWN
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定将某个对象传递给代表已配置的光纤通道主机总线适配器的管道（pipeline）。

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

### -SanName
指定要与光纤通道主机总线适配器关联的虚拟存储区域网络（SAN）的名称。

```yaml
Type: String
Parameter Sets: VMName And Only SAN, Object And Only SAN
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMFibreChannelHba
指定要配置的 Fibre Channel 主机总线适配器。

```yaml
Type: VMFibreChannelHba
Parameter Sets: Object And Generate WWN, Object And Manual WWN, Object And Only SAN
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要设置虚拟光纤通道主机总线适配器参数的虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases:

Required: True
Position: 0
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

### -WorldWideNodeNameSetA
指定与光纤通道主机总线适配器关联的地址集A的全球唯一节点名称（World Wide Node Name）。

```yaml
Type: String
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases: Wwnn1

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWideNodeNameSetB
指定与光纤通道主机总线适配器相关联的地址集B的World Wide Node名称（即网络地址）。

```yaml
Type: String
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases: Wwnn2

Required: True
Position: 3
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortNameSetA
指定与光纤通道主机总线适配器关联的地址集A的全球通用端口号（World Wide Port Name）。

```yaml
Type: String
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases: Wwpn1

Required: True
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortNameSetB
指定与光纤通道主机总线适配器关联的地址集B的全球通用端口号（World Wide Port）名称。

```yaml
Type: String
Parameter Sets: VMName And Only SAN, VMName And Generate WWN, VMName And Manual WWN
Aliases: Wwpn2

Required: True
Position: 4
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMFibreChannelHba

## 备注

## 相关链接

