---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/get-dtc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-Dtc
---

# Get-Dtc

## 摘要
获取 DTC 实例。

## 语法

```
Get-Dtc [-DtcName <String>] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-Dtc` cmdlet 可用于获取在主机上运行的分布式事务协调器（DTC）实例。可以使用 `DtcName` 参数来指定特定的 DTC 实例。

## 示例

### 示例 1：获取一个 DTC 实例
```
PS C:\> Get-Dtc
DtcName           : Local
KtrmEndpointCid   : b6628c9f-46ff-404d-a0fa-62657cb828af
OleTxEndpointCid  : f3027ea1-4ee5-45b5-a01c-06f41221111b
Status            : Started
UisEndpointCid    : e9385758-8092-4dd7-8b09-587aa427a58e
VirtualServerName : Contoso093
XAEndpointCid     : ced49d85-82a9-49d9-a6ee-8c5b4bd7b5bd

DtcName           : MSDTC-Contoso093DTC1
KtrmEndpointCid   :
OleTxEndpointCid  : 04c1c8e4-4810-4dc5-945b-b1cb2c9a2cc4
Status            : Started
UisEndpointCid    : 9a8d3a2f-c28c-4bb6-91fd-8378492bf6a9
VirtualServerName : Contoso093DTC1
XAEndpointCid     : 956d64a7-a307-4aaa-a5d9-10e31f6c51fa

DtcName           : MSDTC-Contoso093DTC2
KtrmEndpointCid   :
OleTxEndpointCid  : ab8eacbf-7b9e-45a5-b61d-b42194d492ea
Status            : Started
UisEndpointCid    : bf1986e4-7c9f-455b-beba-4b8f9fb431ad
VirtualServerName : Contoso093DTC2
XAEndpointCid     : 2833ac93-f291-4fa2-b413-a7b67f7529c1
```

这个命令用于获取一个 DTC（诊断跟踪组件）实例。该命令没有指定 **DtcName** 参数，因此该 cmdlet 会获取本地的 DTC 实例。

### 示例 2：获取本地的 DTC 实例
```
PS C:\> Get-Dtc -DtcName "Local"
DtcName           : Local
KtrmEndpointCid   : b6628c9f-46ff-404d-a0fa-62657cb828af
OleTxEndpointCid  : f3027ea1-4ee5-45b5-a01c-06f41221111b
Status            : Started
UisEndpointCid    : e9385758-8092-4dd7-8b09-587aa427a58e
VirtualServerName : Contoso093
XAEndpointCid     : ced49d85-82a9-49d9-a6ee-8c5b4bd7b5bd
```

此命令用于获取本地的 DTC（诊断测试工具）实例。

## 参数

### -AsJob
将此cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中执行其他操作。要管理该作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

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

### -DtcName
指定要在主机上获取的 DTC（诊断工具集）实例。如果您没有指定此参数，或者指定了“Local”值，那么此 cmdlet 将获取主机的本地 DTC 实例。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值为 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算一个最优的节流限制。该节流限制仅适用于当前的 cmdlet，而不适用于整个会话或计算机本身。

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

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Install-Dtc](./Install-Dtc.md)

[Start-Dtc](./Start-Dtc.md)

[停止 DTC 功能](./Stop-Dtc.md)

[Test-Dtc](./Test-Dtc.md)

[Uninstall-Dtc](./Uninstall-Dtc.md)

