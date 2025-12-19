---
description: 使用此主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Iscsi.Target.Commands.dll-Help.xml
Module Name: IscsiTarget
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iscsitarget/set-iscsiservertarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IscsiServerTarget
---

# 设置 IscsiServerTarget

## 摘要
修改指定iSCSI目标的设置。

## 语法

### TargetName（默认值）
```
Set-IscsiServerTarget [-TargetName] <String> [-TargetIqn <Iqn>] [-Description <String>] [-Enable <Boolean>]
 [-EnableChap <Boolean>] [-Chap <PSCredential>] [-EnableReverseChap <Boolean>] [-ReverseChap <PSCredential>]
 [-MaxReceiveDataSegmentLength <Int32>] [-FirstBurstLength <Int32>] [-MaxBurstLength <Int32>]
 [-ReceiveBufferCount <Int32>] [-EnforceIdleTimeoutDetection <Boolean>] [-InitiatorIds <InitiatorId[]>]
 [-PassThru] [-ComputerName <String>] [-Credential <PSCredential>] [<CommonParameters>]
```

### InputObject
```
Set-IscsiServerTarget -InputObject <IscsiServerTarget> [-TargetIqn <Iqn>] [-Description <String>]
 [-Enable <Boolean>] [-EnableChap <Boolean>] [-Chap <PSCredential>] [-EnableReverseChap <Boolean>]
 [-ReverseChap <PSCredential>] [-MaxReceiveDataSegmentLength <Int32>] [-FirstBurstLength <Int32>]
 [-MaxBurstLength <Int32>] [-ReceiveBufferCount <Int32>] [-EnforceIdleTimeoutDetection <Boolean>]
 [-InitiatorIds <InitiatorId[]>] [-PassThru] [-ComputerName <String>] [-Credential <PSCredential>]
 [<CommonParameters>]
```

## 描述
`Set-IscsiServerTarget` cmdlet 用于修改 iSCSi 目标的设置；如果指定了 `PassThru` 参数，该 cmdlet 会返回相应的 iSCSi 目标对象。

## 示例

### 示例 1：移除与目标相关联的所有发起者
```
PS C:\> Set-IscsiServerTarget -TargetName "Test" -InitiatorId @()
```

这个示例会删除所有与名为“Test”的目标相关联的启动器。

### 示例 2：修改目标的描述
```
PS C:\> Set-IscsiServerTarget -TargetName "TargetOne" -Description "Target for initiator Appsvr"
```

这个例子为名为“TargetOne”的目标设置了描述属性，该目标的发起者是Appsvr。

### 示例 3：配置正向 CHAP（Challenge-Handshake Authentication）
```
PS C:\> $password = ConvertTo-SecureString -String "passwordpass" -AsPlainText -Force



PS C:\> $chap = New-Object -ComObject System.Management.Automation.PSCredential("user", $password)



PS C:\> Set-IscsiServerTarget -TargetName "T1" -EnableChap $True -Chap $chap
```

这个示例启用并设置了目标设备T1上的正向CHAP（Challenge-Handshake Authentication）认证机制，使用用户名“user”和密码作为认证凭据。

### 示例 4：为目标分配发起者 ID
```
PS C:\> Set-IscsiServerTarget -TargetName "Test" -InitiatorId @("IPAddress:10.10.1.10","IPAddress:10.10.1.11")
```

这个例子为同一个目标分配了多个ID。

### 示例 5：为所有尝试连接到该目标的发起者分配一个目标
```
PS C:\> Set-IscsiServerTarget -TargetName "Test" -InitiatorId "IQN:*"
```

这个示例会将目标资源分配给所有尝试连接到该目标的启动器。由于在启动器进行连接时不会对目标资源进行任何验证，因此在使用这种配置时必须非常谨慎。这种配置在排查连接问题时最为有用，因为它可以避免目标资源与启动器之间的错误匹配（即“目标-启动器分配错误”）。

## 参数

### -Chap
指定用于挑战握手认证协议（Challenge Handshake Authentication Protocol，简称CHAP）的用户名和密码的设置。如果尚未启用CHAP，请将该参数与*EnableChap*参数一起使用。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
如果此cmdlet在远程计算机上运行，则会指定该远程计算机的名称或IP地址。

如果此cmdlet是在集群配置上运行的，则指定集群资源组的网络名称或集群节点的名称。

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

### -Credential
指定在连接到远程计算机时所需的凭据信息。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
为 iSCSI 目标指定一个描述信息。

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

### -Enable
用于确定指定的 iSCSI 目标是否已启用或已禁用。

如果您指定值为 `$True`，则目标会被启用。如果目标已经处于启用状态，则不会发生任何操作。

如果您指定值为 `$False`，则该目标将被禁用。如果该目标已经被禁用了，则不会发生任何操作。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -EnableChap
指定是否为iSCSI目标启用CHAP（Challenge-Handshake Authentication，挑战握手认证）功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnableReverseChap
指定是否为iSCSI目标启用了反向CHAP（Reverse CHAP）功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -EnforceIdleTimeoutDetection
指定是否强制检测空闲时间超时情况。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -FirstBurstLength
指定第一个数据包（或传输段）的长度。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InitiatorIds
指定要分配给 iSCSI 目标的 iSCSI 启动器标识符（ID）。

要将一个LUN或VHD分配给iSCSI发起器，首先需要创建一个iSCSI目标。在将目标分配给发起器之后，再将一个LUN与该目标关联起来。该参数的格式为“IdType:Value”。该参数可接受的值包括：DNSName、IPAddress、IPv6Address、IQN和MACAddress。

```yaml
Type: InitiatorId[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -InputObject
从输入管道中接收一个 iSCSI 目标对象。

```yaml
Type: IscsiServerTarget
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MaxBurstLength
指定最大突发长度（即数据包连续传输的最大长度）。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -MaxReceiveDataSegmentLength
指定接收方数据段的最大长度。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -ReceiveBufferCount
指定接收方缓冲区的数量。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ReverseChap
指定反向CHAP认证的用户名和密码。如果尚未启用反向CHAP功能，请将该参数与*EnableReverseChap*参数一起使用。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetIqn
指定目标 iSCSI 合格名称（IQN）。

```yaml
Type: Iqn
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定iSCSI目标的名称。在此之后目标名称无法更改。该参数可用于筛选出特定的iSCSI目标对象。

```yaml
Type: String
Parameter Sets: TargetName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

```cpp
### Microsoft.Iscsi.Target Commands.IscsiServerTarget
```

## 输出

```cpp
### Microsoft.Iscsi.Target Commands.IscsiServerTarget
```

## 备注

## 相关链接

[ConvertTo-SecureString](https://go.microsoft.com/fwlink/p/?LinkId=113291)

[新对象](https://go.microsoft.com/fwlink/p/?LinkId=113355)

[Get-IscsiServerTarget](./Get-IscsiServerTarget.md)

[New-IscsiServerTarget](./New-IscsiServerTarget.md)

[Remove-IscsiServerTarget](./Remove-IscsiServerTarget.md)

